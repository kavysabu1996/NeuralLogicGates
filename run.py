import argparse
import numpy as np
import tensorflow as tf

model_weights = {
                    "AND" : "AND_gate/and_logic_gate.h5",
                    "NOR" : "NOR_gate/nor_logic_gate.h5",
                    "OR"  : "OR_gate/or_logic_gate.h5"
                }

def predict_output(gate, inputs):
    model = tf.keras.models.load_model(model_weights[gate.upper()])    
    inputs = inputs[np.newaxis, ...]
    prediction = model.predict(inputs)
    return int(np.squeeze(prediction.round()))

parser = argparse.ArgumentParser(description="load gate weights")
parser.add_argument('--gate', type=str)
parser.add_argument('--input', nargs='+', type=float)

args = parser.parse_args()

prediction = predict_output(args.gate, np.array(args.input))
print("output for '{}' logic gate is {}".format(args.gate, prediction))



