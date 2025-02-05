from tqdm import tqdm
import tensorflow as tf
import threading
import multiprocessing as mp

def tokenize(ds_obj, mod_obj, max_length=512, batch_size=8,num_cores=96):
    if ds_obj.gpt_sentence is None:
        raise ValueError("Please run dataset_loadqa() and datasetgpt() first before processing.")
    def split_into_chunks(lst, n_chunks):
        n = len(lst)
        n_chunks = min(n, n_chunks)
        k, m = divmod(n, n_chunks)
        return [lst[i * k + min(i, m): (i + 1) * k + min(i + 1, m)] for i in range(n_chunks)]

    def tokenize_batch(batch,max_length=max_length):
        data = mod_obj.tokenizer(batch, padding=True, truncation=True, return_tensors='tf', max_length=max_length)
        return data["input_ids"], data["attention_mask"]

    sentences = ds_obj.gpt_sentence

    # Split into parallel batches
    batches = split_into_chunks(sentences, num_cores)

    # Process batches in parallel
    with mp.Pool(num_cores) as pool:
        batch_results = pool.map(tokenize_batch, batches)

    # Aggregate results
    all_inputs, all_masks, = [], []
    for batch_inputs, batch_masks in batch_results:
        all_inputs.extend(batch_inputs)
        all_masks.extend(batch_masks)

    # Convert to TensorFlow Dataset
    dataset = ds_obj.create_tf_dataset(
        tf.convert_to_tensor(all_inputs),
        tf.convert_to_tensor(all_masks)
    )

    # Now use dataset for training
    dataset = dataset.batch(batch_size).prefetch(tf.data.AUTOTUNE)
    ds_obj.tf_dataset = dataset
    
def multi_run(tasks:list):
    threads = []
    for func in tasks:
        t = threading.Thread(target=func)
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()