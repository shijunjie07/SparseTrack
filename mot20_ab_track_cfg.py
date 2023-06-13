from detectron2.config import LazyCall as L
from omegaconf import OmegaConf
from .datasets.builder import build_test_loader
from .models.model_utils import get_model

# build dataloader
dataloader = OmegaConf.create()
dataloader.test = L(build_test_loader)(
    test_size = (896, 1600), 
    infer_batch = 1 # for tracking process frame by frame 
)
 
# build model
model = L(get_model)(
    model_type = 'yolox',
    depth = 1.33,
    width = 1.25,
    num_classes = 1,
    confthre = 0.01,
    nmsthre = 0.7
)

# build train cfg 
train = dict(
    output_dir="./yolox_mix20_ablation",
    init_checkpoint="/data/zelinliu/sparsetrack/pretrain/bytetrack_20_ablation.pth.tar",
    # model ema
    model_ema = dict(
        enabled=False,
        use_ema_weights_for_eval_only = False,
        decay = 0.9998,
        device = "cuda",
        after_backward = False
    ),
    device="cuda",
)

# build tracker
track = dict(
    experiment_name = "yolox_mix20_ablation_det",
    track_thresh = 0.6,
    track_buffer = 60,
    match_thresh = 0.7,
    min_box_area = 100,
    down_scale = 4,
    depth_levels = 1,
    depth_levels_low = 8,
    confirm_thresh = 0.7,
    mot20 = True,
    byte = False,
    deep = True,
    fp16 = True,
    fuse = True,
    val_ann = "val_half.json"
)
 
 
 
 





