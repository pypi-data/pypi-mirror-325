# Workers

Methods:

- <code title="post /api/workers/{id}">client.workers.<a href="./src/brainbase/resources/workers/workers.py">create</a>(id, \*\*<a href="src/brainbase/types/worker_create_params.py">params</a>) -> None</code>
- <code title="get /api/workers/{id}">client.workers.<a href="./src/brainbase/resources/workers/workers.py">retrieve</a>(id) -> None</code>
- <code title="get /api/workers">client.workers.<a href="./src/brainbase/resources/workers/workers.py">list</a>() -> None</code>
- <code title="delete /api/workers/{id}">client.workers.<a href="./src/brainbase/resources/workers/workers.py">delete</a>(id) -> None</code>

## Deployments

### Voice

Methods:

- <code title="post /api/workers/{workerId}/deployments/voice">client.workers.deployments.voice.<a href="./src/brainbase/resources/workers/deployments/voice.py">create</a>(worker_id, \*\*<a href="src/brainbase/types/workers/deployments/voice_create_params.py">params</a>) -> None</code>
- <code title="get /api/workers/{workerId}/deployments/voice/{deploymentId}">client.workers.deployments.voice.<a href="./src/brainbase/resources/workers/deployments/voice.py">retrieve</a>(deployment_id, \*, worker_id) -> None</code>
- <code title="put /api/workers/{workerId}/deployments/voice/{deploymentId}">client.workers.deployments.voice.<a href="./src/brainbase/resources/workers/deployments/voice.py">update</a>(deployment_id, \*, worker_id, \*\*<a href="src/brainbase/types/workers/deployments/voice_update_params.py">params</a>) -> None</code>
- <code title="get /api/workers/{workerId}/deployments/voice">client.workers.deployments.voice.<a href="./src/brainbase/resources/workers/deployments/voice.py">list</a>(worker_id) -> None</code>
- <code title="delete /api/workers/{workerId}/deployments/voice/{deploymentId}">client.workers.deployments.voice.<a href="./src/brainbase/resources/workers/deployments/voice.py">delete</a>(deployment_id, \*, worker_id) -> None</code>

## Flows

Methods:

- <code title="post /api/workers/{workerId}/flows">client.workers.flows.<a href="./src/brainbase/resources/workers/flows.py">create</a>(worker_id, \*\*<a href="src/brainbase/types/workers/flow_create_params.py">params</a>) -> None</code>
- <code title="get /api/workers/{workerId}/flows/{flowId}">client.workers.flows.<a href="./src/brainbase/resources/workers/flows.py">retrieve</a>(flow_id, \*, worker_id) -> None</code>
- <code title="put /api/workers/{workerId}/flows/{flowId}">client.workers.flows.<a href="./src/brainbase/resources/workers/flows.py">update</a>(flow_id, \*, worker_id, \*\*<a href="src/brainbase/types/workers/flow_update_params.py">params</a>) -> None</code>
- <code title="get /api/workers/{workerId}/flows">client.workers.flows.<a href="./src/brainbase/resources/workers/flows.py">list</a>(worker_id) -> None</code>
- <code title="delete /api/workers/{workerId}/flows/{flowId}">client.workers.flows.<a href="./src/brainbase/resources/workers/flows.py">delete</a>(flow_id, \*, worker_id) -> None</code>
