import tensorflow as tf

ones = tf.constant([[1,2,2],[2,2,2],[3,2,2], [4,2,2]])
# rs = tf.reshape(ones, [2, -1])
with tf.Session() as s:
    print(s.eval())

    
