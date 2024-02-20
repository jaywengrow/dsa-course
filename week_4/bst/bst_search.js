// START:P1
function search(searchValue, node) {
    if (!node || node.value === searchValue) {
      return node;
    }
  
    if (searchValue < node.value) {
      return search(searchValue, node.leftChild);
    } else {
      return search(searchValue, node.rightChild);
    }
  }
  // END:P1
  export default search;
  