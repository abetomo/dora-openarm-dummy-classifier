# Copyright 2026 Enactic, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""dora-rs node that mimics classifier for testing."""

import dora
import pyarrow as pa
import random


def main():
    """Mimics dora-openarm-classifier."""
    node = dora.Node()
    frame = 0
    for event in node:
        if event["type"] != "INPUT":
            continue

        # Main process
        event_id = event["id"]
        if event_id != "image":
            continue

        frame += 1
        score = random.random()
        if score > 0.7:
            verdict = "SUCCESS"
        else:
            verdict = "FAIL"
        node.send_output(
            "result",
            pa.array([score], type=pa.float32()),
            metadata={"verdict": verdict, "frame": frame},
        )


if __name__ == "__main__":
    main()
