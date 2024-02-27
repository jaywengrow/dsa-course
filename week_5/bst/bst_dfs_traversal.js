function dfsTraverse(node) {
  if (!node) { return; }

  console.log(node.value);
  dfsTraverse(node.leftChild);
  dfsTraverse(node.rightChild);
}

export default dfsTraverse;
  
