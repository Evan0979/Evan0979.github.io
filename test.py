def get_label(pic_name):
    # 請取出 label 並轉成數字
    # EX: Claude_Monet_1.jpg -> Claude_Monet -> 1

    #從最右邊開始找分割符並將畫家名拆出來放
    sep_pic_name = pic_name.rpartition("_")
    #e.g.: Albrecht_Du_rer_2 -> ('Albrecht_Du_rer', '_', '2')
    pic_name = sep_pic_name[0]

    #回傳對應之label
    label = author_dict[pic_name]

    return label


def get_path(dir, pic_name):
    # 請將路徑合併
    # EX: ./train_resized/ + Claude_Monet_1.jpg => ./train_resized/Claude_Monet_1.jpg
    path = os.path.join(dir, pic_name)

    return path


def make_paths_label(dir):
    img_list = os.listdir(dir)
    paths = []
    labels = []

    # 將preprocess完成的 path、label 用 for 迴圈放入 paths 和 labels
    for path in img_list:
        path_append = get_path(dir, path)
        label_append = get_label(path)
        paths.append(path_append)
        labels.append(label_append)

    # 將 labels 轉成 onehot
    # todo
    class_weights = class_weight.compute_class_weight('balanced',classes=np.unique(labels),y=labels)
    class_weights_dict = {i : class_weights[i] for i in range(len(class_weights))}
    onehot_labels = keras.utils.to_categorical(labels, num_classes)
    return paths, onehot_labels, class_weights_dict
