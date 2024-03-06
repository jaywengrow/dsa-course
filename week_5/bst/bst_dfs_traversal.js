function dfsTraverse(node) {
  if (!node) { return; }

  dfsTraverse(node.leftChild);
  dfsTraverse(node.rightChild);
  console.log(node.value);
}

export default dfsTraverse;
  
