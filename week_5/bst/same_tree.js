function sameTree(firstNode, secondNode) {
  if (!firstNode && !secondNode) { return true; }
  if ((firstNode && !secondNode) || (!firstNode && secondNode)) { return false;}

  return (firstNode.value === secondNode.value && 
    sameTree(firstNode.leftChild, secondNode.leftChild) && 
    sameTree(firstNode.rightChild, secondNode.rightChild));
}

export default sameTree;
