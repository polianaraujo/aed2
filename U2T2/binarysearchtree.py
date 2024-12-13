from binarysearchtree import *
import plotly.graph_objs as go
import pytest
import numpy as np
import matplotlib.pyplot as plt
from time import time
from scipy.stats import t

# Classe do Nó
class Node:
    """
    A class representing a node in a binary search tree.

    Attributes:
    - value: the value of the node
    - left_child: the left child of the node
    - right_child: the right child of the node
    """

    def __init__(self, value):
        """
        Initializes a new instance of the Node class.

        Args:
        - value: the value of the node
        """
        self.value = value
        self.left_child = None
        self.right_child = None

# Classe da Árvore
class BST:
    """
    A class representing a binary search tree.

    Attributes:
    - root: the root node of the tree
    """

    def __init__(self):
        """
        Initializes a new instance of the BST class.
        """
        self.root = None

    def add(self, value):
        """
        Adiciona um novo nó com o valor dado à árvore.

        Args:
        - value: o valor do nó que será adicionado.
        """
        if self.root is None:
            # Se a raiz ainda não existe, crie-a
            self.root = Node(value)
        else:
            # Encontre o lugar certo e insira um novo valor
            self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):
        """
        A helper method to recursively traverse the tree and find the correct position to add the new node.

        Args:
        - current_node: the current node to traverse
        - value: the value of the node to add
        """
        if value <= current_node.value:
            # Go to the left
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._add_recursive(current_node.left_child, value)
        else:
            # Go to the right
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._add_recursive(current_node.right_child, value)

    def _contains(self, current_node, value):
        """
        Um método auxiliar para percorrer recursivamente a árvore e encontrar o nó com o valor fornecido.

        Args:
        - current_node: o nó atual a ser percorrido
        - value: o valor a ser procurado

        Returns:
        - Verdadeiro se um nó com o valor fornecido for encontrado, Falso caso contrário
        """
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        return self._contains(current_node.right_child, value)

    def contains(self, value):
        """
        Verifica se um nó com o valor fornecido está presente na árvore.

        Args:
        - value: o valor procurado.

        Returns:
        - Verdadeiro se um nó com o valor fornecido for encontrado, Falso caso contrário
        """
        return self._contains(self.root, value)

    def plot(self):
        """
        Plota a árvore de busca binária usando Plotly.
        """
        if self.root is None:
            print("The tree is empty!")
            return

        # Initialize lists for coordinates and connections
        node_coords = []
        lines = []

        # Função auxiliar para percorrer a árvore e preencher as listas de coordenadas e conexões
        def _plot_recursive(node, x, y, offset):
            if node is not None:
                node_coords.append((x, y, node.value))
                if node.left_child is not None:
                    new_x = x - offset
                    new_y = y - 1
                    lines.append((x, y, new_x, new_y))
                    _plot_recursive(node.left_child, new_x, new_y, offset / 2)
                if node.right_child is not None:
                    new_x = x + offset
                    new_y = y - 1
                    lines.append((x, y, new_x, new_y))
                    _plot_recursive(node.right_child, new_x, new_y, offset / 2)

        # Percorrer a árvore começando pelo nó raiz
        _plot_recursive(self.root, x=0, y=0, offset=0.5)

        # Crie um gráfico de dispersão para os nós
        node_trace = go.Scatter(x=[x for x, y, _ in node_coords],
                                y=[y for _, y, _ in node_coords],
                                text=[str(val) for _, _, val in node_coords],
                                mode='markers+text',
                                textposition='top center',
                                marker=dict(symbol='circle',
                                            size=20,
                                            color='darkblue'))

        # Crie um gráfico de dispersão para as conexões entre os nós
        line_trace = go.Scatter(x=sum([[x1, x2, None] for x1, y1, x2, y2 in lines], []),
                                y=sum([[y1, y2, None] for x1, y1, x2, y2 in lines], []),
                                mode='lines',
                                line=dict(color='black'))

        # Combine os dois gráficos de dispersão
        layout = go.Layout(title='',
                           xaxis=dict(title='', showgrid=False, zeroline=False, showticklabels=False),
                           yaxis=dict(title='', showgrid=False, zeroline=False, showticklabels=False),
                           showlegend=False)

        fig = go.Figure(data=[node_trace, line_trace], layout=layout)
        fig.show()
