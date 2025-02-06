# Copyright (c) 2025, IRIS-HEP
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import uproot
import awkward as ak
import dask_awkward as dak 
import logging 

def to_awk(deliver_dict, dask=False, **uproot_kwargs):
    """
    Load an awkward array from the deliver() output with uproot or uproot.dask.

    Parameters:
        deliver_dict (dict): Returned dictionary from servicex.deliver()
                            (keys are sample names, values are file paths or URLs).
        dask (bool):        Optional. Flag to load as dask-awkward array. Default is False
        **uproot_kwargs :   Optional. Additional keyword arguments passed to uproot.dask or uproot.iterate

    
    Returns:
        dict: keys are sample names and values are awkward arrays or dask-awkward arrays.
    """
  
    awk_arrays = {}

    for sample, paths in deliver_dict.items():
        try:
            if dask:
                # Use uproot.dask to handle URLs and local paths lazily 
                awk_arrays[sample] = uproot.dask(paths, library="ak", **uproot_kwargs)
            else:
                # Use uproot.iterate to handle URLs and local paths files in chunks
                tmp_arrays = list(uproot.iterate(paths, library="ak", **uproot_kwargs))
                # Merge arrays
                awk_arrays[sample] = ak.concatenate(tmp_arrays) 

        except Exception as e:
            # Log the exception pointing at the user's code 
            msg=f"\nError loading sample: {sample}"
            logging.error(msg, exc_info=True, stacklevel=2)
            # Mark the sample as failed
            awk_arrays[sample] = None

    return awk_arrays