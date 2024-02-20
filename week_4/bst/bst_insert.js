// START:P1
import TreeNode from './bst_node.js';

function insert(value, node) {
  if (value < node.value) {
    if (!node.leftChild) {
      node.leftChild = new TreeNode(value);
    } else {
      insert(value, node.leftChild);
    }
  } else if (value > node.value) {
    if (!node.rightChild) {
      node.rightChild = new TreeNode(value);
    } else {
      insert(value, node.rightChild);
    }
  }
}
// END:P1
export default insert;
