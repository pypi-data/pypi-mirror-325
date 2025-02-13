import matplotlib.pyplot as plt
import networkx
import pickle
import copy
import matplotlib.animation
import numpy as np
from sparse_transform.qsft.utils.general import qary_vec_to_dec

def initialize_graph(b):
    B =  networkx.Graph()
    check_nodes = [i for i in range (3 * (2 ** b))]
    B.add_nodes_from(check_nodes, bipartite=0)  # Add the node attribute "bipartite"
    return B, check_nodes

def get_positions(B, positions, check_nodes, b):
    pos = networkx.bipartite_layout(B, check_nodes, align="horizontal")
    if b <= 4:
        dist = pos[1] - pos[0]
        for i in range(2 ** b):
            pos[i] = pos[i] - 2*dist
            pos[i + 2*(2 ** b)] = pos[i + 2*(2 ** b)] + 2*dist
    else:
        sec_width = pos[len(pos)//3] - pos[0]
        dist = sec_width / (2 ** 4)
        dist_y = dist[::-1]*1.8
        left_start = pos[0] - 2*dist
        center_start = pos[len(pos)//3]
        right_start = pos[2*(len(pos)//3)] + 2*dist
        for i in range(2 ** b):
            offset = (i % (2 ** 4)) * dist + (i // (2 ** 4)) * dist_y
            pos[i] = left_start + offset
            pos[i + 2*(2 ** b)] = right_start + offset
            pos[i + (2 ** b)] = center_start + offset
    return pos

def draw(B, variable_nodes, check_nodes, b, states, ax, edge_list):
    pos = get_positions(B, variable_nodes, check_nodes, b)
    all_edges = B.edges()
    edges_to_print = [e for e in all_edges if e not in edge_list] + list(edge_list)
    edge_color = ['grey'] * (len(edges_to_print) - len(edge_list)) + ['black'] * len(edge_list)
    networkx.draw(B,
                  pos=pos,
                  with_labels=False,
                  node_color=states + ['black'] * len(variable_nodes),
                  node_size=20,
                  ax=ax,
                  edgelist=edges_to_print,
                  edge_color=edge_color,
                  )


def get_new_singletons(iter_updates, b):
    step1_edges = set()
    step2_edges = set()
    new_variable_nodes = []
    states = [0] * (3 * (2 ** b))
    for i in range(3):
        for j in range(2 ** b):
            check = i*(2 ** b) + j
            node_val = iter_updates[(i, j)] if type(iter_updates[(i, j)]) == int else 1
            if node_val == 0:
                states[check] = "yellow"
            elif node_val == 2:
                states[check] = "red"
            else:
                states[check] = "green"
                k = tuple(iter_updates[(i, j)].astype(int))
                new_variable_nodes.append(k)
                step1_edges.add((check, k))
                for (i_other, j_other) in iter_updates[k]:
                    step2_edges.add(((i_other * (2 ** b)) + j_other, k))
    step2_edges = step2_edges - step1_edges
    return set(new_variable_nodes), states, step1_edges, step2_edges

def update_graph(B, variable_nodes, new_edges):
    if len(variable_nodes) > 0:
        B.add_nodes_from(variable_nodes, bipartite=1)
    B.add_edges_from(new_edges)

def draw_nmse(ax, trajectory, frame):
    ax.plot(range(0, (frame // 2) + 1), [1] + trajectory[:frame // 2], )
    ax.set_xlabel("Iteration")
    ax.set_ylabel("NMSE")
    ax.set_xlim(0, len(trajectory))
    ax.set_ylim(0, 1)

def draw_interact(ax, interactions, frame):
    ax.barh(range(len(interactions)), [x[1] for x in interactions[::-1]],
            color=['red' if x[1] < 0 else 'green' for x in interactions[::-1]])
    ax.set_yticks([])
    ax.set_yticklabels([])  # No labels as requested
    ax.set_xlabel('Interaction Value')
    ax.set_xlim(-1,1)
    ax.set_xticks([-1, 0, 1])

def get_interact_vals(result):
    signal_w_hat = {}
    for k, _, _ in result:
        signal_w_hat[tuple(k)] = 0
    topk = []
    topk.append([([],0)])
    curr_iter = 0
    for k, value, iter_step in result:
        signal_w_hat[tuple(k)] = signal_w_hat.get(tuple(k), 0) + np.real(value)
        if iter_step > curr_iter:
            curr_iter = iter_step
            gwht_in_order = [(k, v) for k, v in signal_w_hat.items()]
            gwht_in_order.sort(key=lambda x: np.abs(signal_w_hat.get(x[0], 0)), reverse=True)
            curr_topk = [([idx for idx, val in enumerate(x[0]) if val != 0], x[1]) for x in gwht_in_order]
            topk.append(curr_topk)
    curr_topk = [([idx for idx, val in enumerate(x[0]) if val != 0], x[1]) for x in gwht_in_order]
    topk.append(curr_topk)
    return topk

if __name__ == '__main__':
    b = 4
    n_iter = 100
    B, check_nodes = initialize_graph(b)
    states = ['green'] * len(check_nodes)
    variable_nodes = set()
    with open("history.pkl", 'rb') as f:
        history = pickle.load(f)
    trajectory = history[-1]
    result = history[-2]
    history = history[:-2]
    iter = 0
    graph_array = []
    while iter < n_iter and len(history[iter]) > 0:
        # Add the new singletons
        new_variable_nodes, states, step1_edges, step2_edges = get_new_singletons(history[iter], b)
        variable_nodes.update(new_variable_nodes)
        # Update the graph
        update_graph(B, variable_nodes, step1_edges)
        graph_array.append({"B": copy.deepcopy(B),
                            "variable_nodes": copy.copy(variable_nodes),
                            "check_nodes": copy.copy(check_nodes),
                            "b": b,
                            "states": copy.copy(states),
                            "edge_list": step1_edges,})
        #draw(B, variable_nodes, check_nodes, b, states)
        # Update the graph
        update_graph(B, [], step2_edges)
        graph_array.append({"B": copy.deepcopy(B),
                            "variable_nodes": copy.copy(variable_nodes),
                            "check_nodes": copy.copy(check_nodes),
                            "b": b,
                            "states": copy.copy(states),
                            "edge_list": step2_edges.union(step1_edges),})
        #draw(B, variable_nodes, check_nodes, b, states)
        iter += 1

    interact_by_iter = get_interact_vals(result)
    def update(frame, graph_array, axs, trajectory, interact):
        [ax.clear() for ax in axs]
        print(f"frame{frame}")
        draw(**graph_array[frame], ax=axs[2])
        draw_nmse(ax=axs[1], trajectory=trajectory, frame=frame)
        draw_interact(ax=axs[0], interactions=interact[frame//2], frame=frame)
        axs[2].set_title(f"Iteration {frame//2}")
        plt.tight_layout()

    fig, ax = plt.subplots(nrows=1, ncols= 3, figsize=(12, 4), width_ratios=[2, 4, 6])
    plt.tight_layout()
    anim = matplotlib.animation.FuncAnimation(fig,
                                              update,
                                              frames=len(graph_array),
                                              interval=300,
                                              repeat=True,
                                              fargs=(graph_array, ax, trajectory, interact_by_iter)
                                              )
    #plt.show()
    anim.save(filename="example.gif", writer="pillow", dpi=300)

