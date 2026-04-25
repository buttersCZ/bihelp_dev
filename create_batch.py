def generate_batch_file(batch: str):
    with open("batch_dev.sql","w") as f:
        f.write(batch)