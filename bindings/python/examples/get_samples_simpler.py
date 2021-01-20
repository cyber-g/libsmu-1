# This example is based on the example given in libsmu.pyx
# for Channel.get_samples()
# https://github.com/analogdevicesinc/libsmu/blob/4d04dcd7615588d8f65d4d1634024435c231ec47/bindings/python/pysmu/libsmu.pyx#L781


from pysmu import Session

SAMPLING_FREQ = 0       # 0 yields the default sampling rate
                        # for ADALM1K, it should be <=100000
CHANNEL = 'A'           # Can be A or B
NUMBER_OF_SAMPLES = 100 # Beware of buffer length ; I do not remmber its length

session = Session(sample_rate=SAMPLING_FREQ)
dev     = session.devices[0]
chan_a  = dev.channels['A']

samples = chan_a.get_samples(NUMBER_OF_SAMPLES)
# Each sample contains a voltage and current value.

print("Sampling rate is:"+str(session.sample_rate))
print(samples)