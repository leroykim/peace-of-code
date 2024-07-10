# Common Representations
- $f(x;\theta)$: a model.
  - $x$: an input to the network.
  - $\theta$: the model parameters.
- $\{x_i, y_i\}^N_1$: $N$ training samples.
  - $x_i$: the $i$-th input instance.
  - $y_i$: the corresponding ground-truth label.
- $W$: a weight matrix to be learned.
- $\hat{\theta}^t = argmin_\theta\sum_{[N]}L^t_{CE}(x_i,y_i;[\theta_{Model_k}, W])$
  - $t$: indicates "teacher" in knowledge distillation.
  - $[N]$: set $\{1,2, \ldots, N\}$.
  - $L^t_{CE}$: Cross-entropy loss.
  - $\theta_{Model_k}$: parameters of $Model$ with $k$ layers of transformers.
# Reference
```bibtex
@article{sun2019patient,
  title={Patient knowledge distillation for bert model compression},
  author={Sun, Siqi and Cheng, Yu and Gan, Zhe and Liu, Jingjing},
  journal={arXiv preprint arXiv:1908.09355},
  year={2019}
}
```