function bfsTraverse(node) {
  const queue = [];
  let currentNode = node;
  queue.push(currentNode);

  while (queue.length > 0) {
    currentNode = queue.shift();

    console.log(currentNode.value);

    if (currentNode.leftChild) {
      queue.push(currentNode.leftChild);
    }
  
    if (currentNode.rightChild) {
      queue.push(currentNode.rightChild);
    }
  }
}

export default bfsTraverse;