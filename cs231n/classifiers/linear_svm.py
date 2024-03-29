import numpy as np
from random import shuffle

def svm_loss_naive(W, X, y, reg):
  """
  Structured SVM loss function, naive implementation (with loops).

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  dW = np.zeros(W.shape) # initialize the gradient as zero

  # compute the loss and the gradient
  num_classes = W.shape[1]
  num_train = X.shape[0]
  loss = 0.0
  for i in range(num_train):
    scores = X[i].dot(W) 
    correct_class_score = scores[y[i]]
    count=0
    for j in range(num_classes):
      if j == y[i]:
            continue
      margin = scores[j] - correct_class_score + 1 # note delta = 1
      if margin > 0:
        count=count+1
        loss += margin
        dW[:,j]+=X[i]
    dW[:,y[i]]-= count*X[i]
  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train
  dW/= num_train

  # Add regularization to the loss.
  loss += reg * np.sum(W * W)
  dW+= reg*W



  #############################################################################
  # TODO:                                                                     #
  # Compute the gradient of the loss function and store it dW.                #
  # Rather that first computing the loss and then computing the derivative,   #
  # it may be simpler to compute the derivative at the same time that the     #
  # loss is being computed. As a result you may need to modify some of the    #
  # code above to compute the gradient.                                       #
  #############################################################################


  return loss, dW


def svm_loss_vectorized(W, X, y, reg):
    
  """
  Structured SVM loss function, vectorized implementation.

  Inputs and outputs are the same as svm_loss_naive.
  """
  num_train=X.shape[0]
  loss = 0.0
  dW = np.zeros(W.shape) # initialize the gradient as zero
  scores = X.dot(W)
  delta= 1.00
  indecies= np.arange(scores.shape[0])
  correct_classes= np.array(scores[indecies,y])
  margins = np.maximum(0, scores - np.matrix(correct_classes).T+ delta)
  margins[indecies,y]= 0
  loss = np.sum(np.sum(margins, axis=1))

  loss /= num_train
  loss += reg * np.sum(W * W)
  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the structured SVM loss, storing the    #
  # result in loss.                                                           #
  #############################################################################

  
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################
    
  coff= np.zeros(margins.shape)
  coff[margins > 0] = 1
  count_incorrect=  np.sum(coff, axis=1)
  coff[np.arange(num_train), y] = -count_incorrect.T
  dW= np.dot(X.T, coff)
    
  dW/= num_train
  dW+= reg*W   
    
  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the gradient for the structured SVM     #
  # loss, storing the result in dW.                                           #
  #                                                                           #
  # Hint: Instead of computing the gradient from scratch, it may be easier    #
  # to reuse some of the intermediate values that you used to compute the     #
  # loss.                                                                     #
  #############################################################################
  
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################

  return loss, dW
