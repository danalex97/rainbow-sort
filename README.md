## Motivation 

Sorting using hardware is an exciting thing to do, as well as the concept of using an adaper over natural phenomenon in order to implement certain algorithms. The experiment is only a simple proof-of-concept implementation.

## Rainbowsort workflow

* Iterate over the array A and determine minimum m and maximum M.
* Choose a strictly increasing function f:[m, M] -> [400, 700].
* Apply f to A, let W = {f(x) | x in A}.
* Compose a light beam having the components with wavelengths in W.
* Project the light beam through a prism, so dispersion happens.
* Observe/retreive the result beam(call it R), which has the components already sorted.
* Apply the inverse of f over the elements of R.

The complexity for sorting itself is constant, but the feed of input and retreival is linear.
Other applications might include constant time for n-th element structures, supposing the I/O is constant.

The prism is a naturally sorting build sort circuit. Back-of-the-envelope calculation: if side of the prism is 10cm and the speed thorough the prism is c/3 ~ 100.000 km/s, then the light takes around 10^-9 to travel through the prism.

For clarity, you might want to reffer to:

* https://en.wikipedia.org/wiki/Refraction
* https://en.wikipedia.org/wiki/Dispersion_(optics)

## Hardware part the setup

The complexity will(obviously) not hold.

The setup:
* Banana Pi
* 4 leds with different frequencies
* slit(improvised by 2 post-it sets)
* 2 lens: biconvex(for focusing), plan-concave(for straighten)
* observation wall(another post-it set)

Simplified workflow:
* Use only refraction for light without actually combining it.
* The output rays are sorted by on horizontal from left to right. (e.g. from red, blue orange, green to red, orange, green, blue - see example image)

<img src="https://github.com/danalex97/rainbow-sort/blob/master/setup/3.jpg" width=250>
<img src="https://github.com/danalex97/rainbow-sort/blob/master/setup/4.jpg" width=250>
<img src="https://github.com/danalex97/rainbow-sort/blob/master/setup/6.jpg" width=250>
<img src="https://github.com/danalex97/rainbow-sort/blob/master/setup/7.jpg" width=250>
<img src="https://github.com/danalex97/rainbow-sort/blob/master/setup/8.jpg" width=250>
<img src="https://github.com/danalex97/rainbow-sort/blob/master/setup/9.jpg" width=250>

## Software part

to do
