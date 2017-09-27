import SimpleITK as sitk


class Deploy:
    def __init__(self, input_volume, output_label):
        self.input_volume = input_volume
        self.output_label = output_label

    def run(self):
        image = sitk.ReadImage(self.input_volume)
        label = sitk.BinaryThreshold(image, 20, 255, 1, 0)
        sitk.WriteImage(label, self.output_label, True)

if __name__ == '__main__':
    import os
    sample_volume = os.path.join('.', 'sample', 'MRHead.nrrd')
    sample_label = os.path.join('.', 'sample', 'MRHead-label.nrrd')
    deployer = Deploy(input_volume=sample_volume, output_label=sample_label)
    deployer.run()

