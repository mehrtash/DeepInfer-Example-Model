import os
import sys
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    #
    parser.add_option("-m", "--ModelName", type="string",
                      help="choose a model from example docker image",
                      dest="model")
    #
    parser.add_option("--InputVolume", type="string",
                      help="Input Volume for Single input models",
                      dest="input_volume")
    parser.add_option("--OutputLabel", type="string",
                      help="Output label path for segmenters.",
                      dest="output_label")
    #
    models = list()
    models.append('threshold')
    #
    (options, args) = parser.parse_args()
    if options.model:
        model = options.model
        if model not in models:
            print('model: {} is not available. You can select from the following models:{}'.format(model, models))
            sys.exit()
        print('model: {}'.format(model))
        if model == 'threshold':
            if not options.input_volume or not options.output_label:
                print('usage error: you must give InputVolume and OutputLabel')
            else:
                input_volume = options.input_volume
                output_label = options.output_label
                if os.path.isfile(input_volume) and os.path.isdir(os.path.dirname(output_label)):
                    from models.threshold.deploy import Deploy
                    print('starting deployment and inference...')
                    deployer = Deploy(input_volume=input_volume, output_label=output_label)
                    deployer.run()
                else:
                    if not os.path.isfile(input_volume):
                        print("could not find path for Input Volume: {}".format(input_volume))
                    if not os.path.isdir(output_label):
                        print("could not find path for Output Folder: {}".format(output_label))

