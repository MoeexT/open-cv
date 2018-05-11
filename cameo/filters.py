#! py -3
# -*- coding: utf-8 -*-

import cv2
import numpy
import utils


def stroke_edges(src, dst, blur_k_size=7, edge_k_size=5):
    if blur_k_size >= 3:
        blurred_src = cv2.medianBlur(src, blur_k_size)
        gray_src = cv2.cvtColor(blurred_src, cv2.COLOR_BGR2GRAY)
    else:
        gray_src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    cv2.Laplacian(gray_src, cv2.CV_8U, gray_src, ksize=edge_k_size)
    normalized_inverse_alpha = (1.0 / 255) * (255 - gray_src)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalized_inverse_alpha

    cv2.merge(channels, dst)


class VConvolutionFilter(object):
    """
    a filter that applies a convolution to V (or all of BGR)
    """

    def __init__(self, kernel):
        self._kernel = kernel

    def apply(self, src, dst):
        """
        apply the filter with a BGR or gray source/destination.
        :param src:
        :param dst:
        :return:
        """
        cv2.filter2D(src, -1, self._kernel, dst)


class SharpenFilter(VConvolutionFilter):
    """a sharpen filter with a 1-pixel radius"""

    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class FindEdgesFilter(VConvolutionFilter):
    """
    an edge-finding filter with a 1-pixel radius.
    """

    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class BlurFilter(VConvolutionFilter):
    """
    a blur filter with a 2-pixel radius.
    """

    def __init__(self):
        kernel = numpy.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04]])
        VConvolutionFilter.__init__(self, kernel)


class EmbossFilter(VConvolutionFilter):
    """
    an emboss filter with a 1-pixel radius.
    """

    def __init__(self):
        kernel = numpy.array([[-2, -1, 0],
                              [-1, 1, 1],
                              [0, 1, 2]])
        VConvolutionFilter.__init__(self, kernel)


class BGRFuncFilter(object):
    # no doc
    def __init__(self, v_func=None, b_func=None, g_func=None, r_func=None, d_type=numpy.uint8):
        length = numpy.iinfo(d_type).max + 1

        self._b_lookup_array = utils.create_lookup_array(
            utils.create_composite_func(b_func, v_func), length)
        self._g_lookup_array = utils.create_lookup_array(
            utils.create_composite_func(g_func, v_func), length)
        self._r_lookup_array = utils.create_composite_func(
            utils.create_composite_func(r_func, v_func), length)

    def apply(self, src, dst):
        """
        apply the filter with a BGR source/destination.
        :param src:
        :param dst:
        :return:
        """
        b, g, r = cv2.split(src)
        print(b.shape, g.shape, r.shape)
        utils.apply_lookup_array(self._b_lookup_array, b, b)
        utils.apply_lookup_array(self._g_lookup_array, g, g)
        utils.apply_lookup_array(self._r_lookup_array, r, r)
        cv2.merge([b, g, r], dst)


class BGRCurveFilter(BGRFuncFilter):
    # no doc
    def __init__(self, v_points=None, b_points=None, g_points=None, r_points=None, d_type=numpy.uint8):
        BGRFuncFilter.__init__(self, utils.create_curve_func(v_points),
                               utils.create_curve_func(b_points),
                               utils.create_curve_func(g_points),
                               utils.create_curve_func(r_points), d_type)


class BGRPortraCurveFilter(BGRCurveFilter):
    # no doc
    def __init__(self, d_type=numpy.uint8):
        BGRCurveFilter.__init__(self, v_points=[(0, 0), (23, 20), (157, 173), (255, 255)],
                                b_points=[(0, 0), (41, 46), (231, 228), (255, 255)],
                                g_points=[(0, 0), (52, 47), (189, 196), (255, 255)],
                                r_points=[(0, 0), (69, 69), (213, 218), (255, 255)],
                                d_type=d_type)

