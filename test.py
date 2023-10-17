import torch


def main():
    B, n, d = 4, 2, 3
    a = torch.arange(B * n * d).reshape(B, n, d)
    print(a, a.shape)
    trans = a.transpose(1, 2)
    print(trans, trans.shape)
    prod = a @ trans
    print(prod, prod.shape)


if __name__ == '__main__':
    main()
