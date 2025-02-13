import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense


class ControlDense(tf.keras.layers.Layer):
    def __init__(self):
        super().__init__()

    def build(self, input_shape):
        self.w = self.add_weight(shape=(input_shape[-1], 1), trainable=True, name="w")
        self.b = self.add_weight(shape=[], trainable=True, name="b", use_resource=False)

    def call(self, inputs):
        with tf.control_dependencies([self.b]):
            return tf.matmul(inputs, self.w)


def main():
    inputs = Input(shape=(32,))
    x = ControlDense()(inputs)
    outputs = Dense(10, activation="softmax")(x)

    model = Model(name="foo", inputs=inputs, outputs=outputs)

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    tf.saved_model.save(model, "output")


if __name__ == "__main__":
    main()
