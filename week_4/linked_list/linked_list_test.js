import Node from './node.js';
import LinkedList from './linked_list.js';

function assertEqual(x, y) {
  if (x === y) {
    console.log('.');
  } else {
    console.log('FAIL');
  }
}

// Merge lists
const listA = new LinkedList();
listA.append(1);
listA.append(4);
listA.append(7);
listA.append(8);
const listB = new LinkedList();
listB.append(2);
listB.append(3);
listB.append(5);
listB.append(6);
let head = listA.merge(listB)

let currentNode = head;

while (currentNode) {
  console.log(currentNode.data);
  currentNode = currentNode.nextNode;
}

