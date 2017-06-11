import coremltools

coreml_model = coremltools.converters.caffe.convert(('alpha_iter_1300.caffemodel', 'alpha_solfer.prototxt'),
                                                    predicted_feature_name='training_index.txt'
                                                    )

coreml_model.save('OCRClassifier.mlmodel')
