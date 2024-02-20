// START:P1
import Node from './node.js';

class LinkedList {
  constructor(firstNode=null) {
    this.firstNode = firstNode;
  }

  read(index) {
    let currentNode = this.firstNode;
    let currentIndex = 0;

    while (currentIndex < index) {
      currentNode = currentNode.nextNode;
      currentIndex += 1;

      if (!currentNode) {
        return null;
      }
    }

    return currentNode.data;
  }

  search(value) {
    let currentNode = this.firstNode;
    let currentIndex = 0;

    while (true) {
      if (currentNode.data === value) {
        return currentIndex;
      }

      currentNode = currentNode.nextNode;

      if (!currentNode) {
        break;
      }

      currentIndex += 1;
    }

    return null;
  }

  append(value) {
    const newNode = new Node(value);

    if (!this.firstNode) {
      this.firstNode = newNode;
      return;
    }

    let currentNode = this.firstNode;

    while (true) {
      if (currentNode.nextNode) {
        currentNode = currentNode.nextNode;
      } else {
        currentNode.nextNode = newNode;
        break;
      }
    }
  }

  recursiveAppend(value, currentNode = null) {
    const newNode = new Node(value);

    if (!this.firstNode) {
      this.firstNode = newNode;
      return;
    }

    if (!currentNode) {
      currentNode = this.firstNode;
    }

    if (currentNode.nextNode) {
      this.recursiveAppend(value, currentNode.nextNode);
    } else {
      currentNode.nextNode = newNode;
    }
  }

  insert(index, value) {
    const newNode = new Node(value);

    if (index === 0) {
      newNode.nextNode = this.firstNode;
      this.firstNode = newNode;
      return;
    }

    let currentNode = this.firstNode;
    let currentIndex = 0;

    while (currentIndex < (index - 1)) {
      currentNode = currentNode.nextNode;
      currentIndex += 1;
    }

    newNode.nextNode = currentNode.nextNode;

    currentNode.nextNode = newNode;
  }

  delete(index) {
    if (index === 0) {
      this.firstNode = this.firstNode.nextNode;
      return;
    }

    let currentNode = this.firstNode;
    let currentIndex = 0;

    while (currentIndex < (index - 1)) {
      currentNode = currentNode.nextNode;
      currentIndex += 1;
    }

    const nodeAfterDeletedNode = currentNode.nextNode.nextNode;
    currentNode.nextNode = nodeAfterDeletedNode;
  }

  printList() {
    let currentNode = this.firstNode;

    while (currentNode) {
      console.log(currentNode.data);
      currentNode = currentNode.nextNode;
    }
  }

  last() {
    let currentNode = this.firstNode;

    while (currentNode.nextNode) {
      currentNode = currentNode.nextNode;
    }

    return currentNode.data;
  }

  recursiveLast(currentNode = null) {
    if (!currentNode) {
      currentNode = this.firstNode;
    }

    if (currentNode.nextNode) {
      return this.recursiveLast(currentNode.nextNode);
    } else {
      return currentNode.data;
    }
  }

  reverse() {
    let previousNode = null;
    let currentNode = this.firstNode;

    while (currentNode) {
      const nextNode = currentNode.nextNode;
      currentNode.nextNode = previousNode;

      previousNode = currentNode;
      currentNode = nextNode;
    }

    this.firstNode = previousNode;
  }

  merge(list) {
    let currentPointer;
    let otherPointer;
    let head;
    let temp;

    if (this.firstNode.data <= list.firstNode.data) {
      head = this.firstNode;
      temp = this.firstNode.nextNode;
      otherPointer = this.firstNode.nextNode;
      currentPointer = list.firstNode;
      this.firstNode.nextNode = currentPointer;
    } else {
      head = list.firstNode;
      temp = list.firstNode.nextNode;
      otherPointer = list.firstNode.nextNode;
      currentPointer = this.firstNode;
      list.firstNode.nextNode = currentPointer;
    }


    while (currentPointer.nextNode) {
      if (currentPointer.nextNode.data <= otherPointer.data) {
        currentPointer = currentPointer.nextNode;
      } else {
        temp = currentPointer.nextNode;
        
        currentPointer.nextNode = otherPointer;
        currentPointer = otherPointer;
        otherPointer = temp;
      }
    }

    currentPointer.nextNode = otherPointer;

    return head;

  }

}
export default LinkedList;
