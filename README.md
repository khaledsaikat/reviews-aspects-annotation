# reviews-aspects-annotation
Manually assign aspects to amazon product reviews

## Aspects count

### headphone100.json
```
Total count:  14
Counter({'sound quality': 76, 'price': 50, 'comfortability': 26, 'quality': 21, 'fit': 20, 'noise cancellation': 14, 'cord': 11, 'design': 11, 'price worthy': 9, 'durability': 8, 'color': 6, 'size': 3, 'delivery time': 3, 'packaging': 2})

Top count 11 with min 5 reviews
Counter({'sound quality': 76,
         'price': 50,
         'comfortability': 26,
         'quality': 21,
         'fit': 20,
         'noise cancellation': 14,
         'cord': 11,
         'design': 11,
         'price worthy': 9,
         'durability': 8,
         'color': 6})
```

### kindle100.json
```
Total count:  24
Counter({'screen': 24, 'apps': 22, 'sound quality': 16, 'price': 14, 'ease of use': 11, 'size': 11, 'browsing': 7, 'response time': 7, 'wifi': 7, 'reading': 7, 'quality': 6, 'battery life': 6, 'streaming': 5, 'shipping time': 5, 'camera': 4, 'ads': 4, 'weight': 4, 'software': 4, 'charging': 3, 'hardware': 3, 'customer service': 3, 'design': 2, 'price worthy': 2, 'functionality': 2})

Top count 14 with min 5 reviews
Counter({'screen': 24,
         'apps': 22,
         'sound quality': 16,
         'price': 14,
         'ease of use': 11,
         'size': 11,
         'browsing': 7,
         'response time': 7,
         'wifi': 7,
         'reading': 7,
         'quality': 6,
         'battery life': 6,
         'streaming': 5,
         'shipping time': 5})
```


### sandisk100.json
```
Total count:  22
Counter({'speed': 38, 'works': 27, 'price': 24, 'storage': 14, 'adapter': 11, 'quality': 9, 'reliability': 7, 'compatibility': 7, 'shipping time': 6, 'packaging': 5, 'size': 4, 'longevity': 4, 'ease of use': 4, 'recording': 3, 'issue': 2, 'durability': 2, 'hardware': 2, 'looks': 1, 'cloud': 1, 'temperature': 1, 'seller': 1, 'software': 1})

Top count 10 with min 5 reviews
Counter({'speed': 38,
         'works': 27,
         'price': 24,
         'storage': 14,
         'adapter': 11,
         'quality': 9,
         'reliability': 7,
         'compatibility': 7,
         'shipping time': 6,
         'packaging': 5})
```

## Inspecting by script


```
from annotation import Annotation

annotation = Annotation()
annotation.loadReviews("headphone100.json")

# Showing annotated aspects name with reviews numbers
annotation.showManualAspects()

# Showing aspects for each line
annotation.showLinesAspects()

# Creating cluster based on aspects
annotation.showAspectsGruopsText()
```

Script has been written on python3
