from transformers import BartConfig

config = BartConfig.from_pretrained('facebook/bart-large')
config.forced_bos_token_id = 0
config.save_pretrained('./config')