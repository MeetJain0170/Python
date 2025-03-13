import numpy as np

def entropy(positives, negatives):
    total = positives + negatives
    if total == 0:  # To avoid division by zero
        return 0
    p_pos = positives / total
    p_neg = negatives / total
    
    # Handling case when probabilities are zero (avoid log(0))
    if p_pos == 0:
        entropy_pos = 0
    else:
        entropy_pos = -p_pos * np.log2(p_pos)
    
    if p_neg == 0:
        entropy_neg = 0
    else:
        entropy_neg = -p_neg * np.log2(p_neg)
    
    return entropy_pos + entropy_neg

def information_gain(parent_entropy, child_nodes):
    total = sum(positives + negatives for positives, negatives in child_nodes)
    
    weighted_entropy = 0
    for positives, negatives in child_nodes:
        weight = (positives + negatives) / total
        weighted_entropy += weight * entropy(positives, negatives)
    
    gain = parent_entropy - weighted_entropy
    return gain

parent_positives = int(input("Enter the number of positives for the parent node: "))
parent_negatives = int(input("Enter the number of negatives for the parent node: "))

parent_entropy = entropy(parent_positives, parent_negatives)
print(f'Parent Entropy: {parent_entropy:.4f}')

num_child_nodes = int(input("Enter the number of child nodes (sub-branches): "))

child_nodes = []
for i in range(num_child_nodes):
    print(f"Child node {i+1}:")
    positives = int(input(f"  Enter the number of positives for child node {i+1}: "))
    negatives = int(input(f"  Enter the number of negatives for child node {i+1}: "))
    child_nodes.append((positives, negatives))

gain = information_gain(parent_entropy, child_nodes)
print(f'Information Gain: {gain:.4f}')
