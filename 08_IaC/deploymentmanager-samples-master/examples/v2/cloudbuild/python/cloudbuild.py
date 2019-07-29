# Copyright 2017 Google Inc. All rights reserved.
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
"""Creates a Cloud Container Builder build."""

import json


def GenerateConfig(context):
  """Generate YAML resource configuration."""

  resources = [{
      'name': 'my-build',
      'action': 'gcp-types/cloudbuild-v1:cloudbuild.projects.builds.create',
      'metadata': {
          'runtimePolicy': ['UPDATE_ALWAYS']
      },
      'properties': {
          'steps': [
              {
                  'name': 'gcr.io/cloud-builders/gcloud',
                  'args': ['deployment-manager',
                           context.properties['resourceToList'],
                           'list']
              }
          ],
          'timeout': '120s'
      }
  }]
  return { 'resources': resources }

