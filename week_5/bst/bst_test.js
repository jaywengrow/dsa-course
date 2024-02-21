import TreeNode from './bst_node.js';
import search from './bst_search.js';
import insert from './bst_insert.js';
import traverse from './bst_traversal.js';
import invert from './bst_invert.js';
import sameTree from './same_tree.js';
import validate from './validate_bst.js';



function assertEqual(x, y) {
  if (x === y) {
    console.log('.');
  } else {
    console.log('FAIL');
  }
}

// Tree Node - Basic
console.log('BST basic');
const node1 = new TreeNode(25);
const node2 = new TreeNode(75);
let root = new TreeNode(50, node1, node2);
assertEqual(root.value, 50);
assertEqual(root.rightChild.value, 75);
assertEqual(root.leftChild.value, 25);

// BST search
console.log('BST search');
assertEqual(search(50, root), root);
assertEqual(search(75, root), node2);
assertEqual(search(25, root), node1);
assertEqual(search(100, root), null);
assertEqual(search(0, root), null);

// BST insertion
console.log('BST insertion');
root = new TreeNode(50);
insert(25, root);
insert(75, root);
insert(60, root);
insert(100, root);
insert(90, root);
insert(5, root);
insert(40, root);
assertEqual(search(50, root).value, 50);
assertEqual(search(25, root).value, 25);
assertEqual(search(75, root).value, 75);
assertEqual(search(60, root).value, 60);
assertEqual(search(100, root).value, 100);
assertEqual(search(90, root).value, 90);
assertEqual(search(5, root).value, 5);
assertEqual(search(40, root).value, 40);


// Traversal
console.log('Traversal');
root = new TreeNode(5);
insert(2, root);
insert(7, root);
insert(1, root);
insert(3, root);
insert(6, root);
insert(8, root);
traverse(root);

// Invert
console.log('Invert');
root = new TreeNode(5);
insert(2, root);
insert(7, root);
insert(1, root);
insert(3, root);
insert(6, root);
insert(8, root);
invert(root);
traverse(root);

// Same Tree
console.log('Same Tree');
const tree1 = new TreeNode(5);
insert(2, tree1);
insert(7, tree1);
insert(1, tree1);
insert(3, tree1);
insert(6, tree1);
insert(8, tree1);

const tree2 = new TreeNode(5);
insert(2, tree2);
insert(7, tree2);
insert(1, tree2);
insert(3, tree2);
insert(6, tree2);
insert(8, tree2);

const tree3 = new TreeNode(5);
insert(2, tree3);
insert(7, tree3);
insert(1, tree3);
insert(3, tree3);
insert(6, tree3);
insert(9, tree3);

assertEqual(sameTree(tree1, tree2), true);
assertEqual(sameTree(tree1, tree3), false);

// Validate BST
console.log("Validate BST");
assertEqual(validate(tree1), true);
invert(tree1);
assertEqual(validate(tree1), false);
const sanityTree = new TreeNode(2);
insert(1, sanityTree);
insert(3, sanityTree);
assertEqual(validate(sanityTree), true);


