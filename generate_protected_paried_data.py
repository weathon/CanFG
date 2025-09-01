def parse(args=None):
    parser = argparse.ArgumentParser()
    # parser.add_argument('--data_path', default='/data_disk/wangtao/mymodel/data/img_align_celeba/', type=str)
    parser.add_argument('--data_path', default='/media/HDD1/wangtao/datatset/img_align_celeba/img_128_align/', type=str)

    parser.add_argument('--lambda_rec', type=float, default=100)
    parser.add_argument('--lambda_gp',  type=float, default=10.0)
    parser.add_argument('--lambda_id', type=float, default=0)
    parser.add_argument('--lambda_em', type=float, default=500)
    parser.add_argument('--lambda_lp', type=float, default=10)

    parser.add_argument('--mode', dest='mode', default='wgan', choices=['wgan', 'lsgan', 'dcgan'])
    parser.add_argument('--epochs', dest='epochs', type=int, default=125, help='# of epochs')
    parser.add_argument('--batch_size', dest='batch_size', type=int, default=64)# todo
    parser.add_argument('--lr', dest='lr', type=float, default=0.0002, help='learning rate')
    parser.add_argument('--beta1', dest='beta1', type=float, default=0.5)
    parser.add_argument('--beta2', dest='beta2', type=float, default=0.999)
    parser.add_argument('--n_d', dest='n_d', type=int, default=4, help='# of d updates per g update')

    parser.add_argument('--b_distribution', dest='b_distribution', default='none',
                        choices=['none', 'uniform', 'truncated_normal'])
    parser.add_argument('--n_samples', dest='n_samples', type=int, default=32 , help='# of sample images')

    parser.add_argument('--gpu', dest='gpu', action='store_true',default=True)
