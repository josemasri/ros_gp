#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
import numpy as np
from ros_gp.srv import AddTwoInts
from scripts.Node import FUNCTION, Node

terminals = ['0', '1', '2']
functions = ['if', '<=']

n_gen: int = 0
pop_size: int = 0
pop = []


def generate_random_ind():
    tree = Node(np.random.randint(0, len(functions) - 1), FUNCTION)
    tree.insert()


def add_two_ints_client(x, y):
    rospy.wait_for_service('genetic_program')
    try:
        genetic_program = rospy.ServiceProxy('genetic_program', AddTwoInts)
        resp1 = genetic_program(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def generate_initial_pop():
    for i in pop_size:
        tree = generate_random_ind()
        pop.append(tree)


def evaluate_pop():
    pass


def select_pop():
    pass


def cross():
    pass


def mutate():
    pass


if __name__ == "__main__":
    n_gen = int(input("Enter the number of generations"))
    pop_size = int(input("Enter the number of individuals"))

    # Generate initial pop
    generate_initial_pop()

    for i in range(n_gen):
        # Eval initial pop
        evaluate_pop()
        # Seleccionar N padres
        select_pop()
        # Cruza por pares
        cross()
        # Mutación de N hijos
        mutate()
