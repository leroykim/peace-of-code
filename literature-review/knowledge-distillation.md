# Knowledge Distillation

## Definition
Methods that distill knowledge from larger deep neural netowkr model(s) to smaller model.

## Concepts
- Teacher-student architecture
- Knowledge
- Logits
- Dark knowledge
- Soft targets
- Hard targets
- Temperature
- Distillation loss
- Student-loss
- Distillation
    - Offline distillation
    - Online distillation
    - Self-distillation

## Graph-Based Distillation
```mermaid
---
title: A generic graph-based distillation (gou2021knowledge)
---
flowchart LR
  data[DATA] --> teacher[Teacher] & student[Student]
  teacher -- Relation Knowledge --> graphs((Graphs))
  graphs -- Distillation --> student
```

Graphs are used for
- Carrier of teacher knowledge
- Controls the message passing of the teacher knowledge

## Quantized Distillation
```mermaid
---
title: A generic quantized distillation (gou2021knowledge)
---
flowchart BT
  large_network[A large network] --Quantization--> student[Low-precision\nstudent network]
  teacher[Full-precision teacher network] -.Quantization.->student
  teacher --Knowledge Transfer--> student

```

## Reference
```bibtex
@article{hinton2015distilling,
  title={Distilling the knowledge in a neural network},
  author={Hinton, Geoffrey and Vinyals, Oriol and Dean, Jeff},
  journal={arXiv preprint arXiv:1503.02531},
  year={2015}
}

@article{gou2021knowledge,
  title={Knowledge distillation: A survey},
  author={Gou, Jianping and Yu, Baosheng and Maybank, Stephen J and Tao, Dacheng},
  journal={International Journal of Computer Vision},
  volume={129},
  number={6},
  pages={1789--1819},
  year={2021},
  publisher={Springer}
}
```