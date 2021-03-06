import os

# Data.
midi_data_path = 'midi_data'
midi_data_valid_path = 'midi_data_valid'
midi_data_valid_repaired_path = 'midi_data_valid_repaired'
midi_data_valid_quantized_path = 'midi_data_valid_quantized'

# Artefacts.
output_dir = 'output'
model_output_dir = 'output_model'
baseline_output_dir = 'output_baseline'


def create_directories():
    dirs = [midi_data_path,
            midi_data_valid_path,
            midi_data_valid_repaired_path,
            midi_data_valid_quantized_path,
            output_dir,
            model_output_dir,
            baseline_output_dir]
    [os.makedirs(d) for d in dirs if not os.path.exists(d)]
