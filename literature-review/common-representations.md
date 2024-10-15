# Common Representations
## Knowledge Distillation on LLM
```bibtex
@article{sun2019patient,
  title={Patient knowledge distillation for bert model compression},
  author={Sun, Siqi and Cheng, Yu and Gan, Zhe and Liu, Jingjing},
  journal={arXiv preprint arXiv:1908.09355},
  year={2019}
}
```
### Vanila Knowledge Distillation
- $f(x;\theta)$: a model.
  - $x$: an input to the network.
  - $\theta$: the model parameters.
- $\{x_i, y_i\}^N_1$: $N$ training samples.
  - $x_i$: the $i$-th input instance.
  - $y_i$: the corresponding ground-truth label.
- $W$: a weight matrix to be learned.
- $h_i = Model(x_i) \in \mathbb{R}^d$: a contextualized embedding.
- $\hat{\theta}^t = argmin_\theta\sum_{[N]}L^t_{CE}(x_i,y_i;[\theta_{Model_k}, W])$
  - $t$: indicates "teacher" in knowledge distillation.
  - $[N]$: set $\{1,2, \ldots, N\}$.
  - $L^t_{CE}$: Cross-entropy loss.
  - $\theta_{Model_k}$: parameters of $Model$ with $k$ layers of transformers.
- $\hat{y_i} = P^t(y_i|x_i) = softmax(\frac{Wh_i}{T}) = softmax(\frac{W\cdot Model_k(x_i;\hat{\theta^t})}{T})$
  - $\hat{y_i}$: soft label.
  - $P^t(\cdot | \cdot)$: probability output.
  - $T$: temperature.
- $L_{DS} = - \sum_{i \in [N]} \sum_{c \in C}[P^t(y_i = c |x_i;\hat{\theta}^t) \cdot logP^s(y_i = c |x_i;\hat{\theta}^s)]$: the distance between the teacher's prediction and the student's prediction.
  - $\hat{\theta}^s$: parameters to be learned for the student model.
  - $c$: a class label.
  - $C$: the set of class labels.
- $L^s_{CE} = - \sum_{i \in [N]} \sum_{c \in C}[\mathbb{1}[y_i=c] \cdot logP^s(y_i = c|x_i;\theta^s)]$: task specific cross-entropy loss.
- $L_{KD} = (1-\alpha)L^s_{}CE + \alpha L_{DS}$

### Patient Knowledge Distillation
