# Daemonsets on Google Kubernetes Engine using Deployment Manager

#### Step 1. Deploying a cluster and cluster-type

The template files that we will use for deploying the cluster in GCP are:

 - cluster.yaml
 - cluster.jinja
 - cluster.jinja.schema

In cluster.yaml, you need to provide the name of the cluster, the GCP zone
where the cluster nodes are deployed and the username/password that you wish
to provide the cluster. You can add/edit the scope of the instances as well
as change the default machine-types in cluster.jinja files. The location of
cluster.yaml and associated dependent files can be found at the root of
`deploymentmanager-samples/example/v2/gke` folder

To create and deploy the cluster and cluster-type, run the following command

    gcloud deployment-manager deployments create cluster --config cluster.yaml


This will create a Google Kubernetes Engine (GKE) cluster and cluster-type
deployment. The GKE cluster will be managed by GCP with username/password
as the auth.


### Step 2. Deploying the daemonset (my-agent) to the deployed cluster in GKE

The template files that we will use for deploying the my-agent (as Daemonsets)
to the GKE cluster are:

 - daemonset.yaml
 - daemonset.jinja.schema
 - daemonset.jinja

The cluster created (via DM templates as step1. or using gcloud directly)
needs to be provided as input to the yaml file properties. Along with this,
the GKE/kubernetes version (1.2 or earlier) can be configured here.
The agent specific properties like the access-key, docker image and custom port
where the agent runs are also configured as a part of the config file.
Please note that this example uses a generic daemonset topology. This needs to
be modifed as per your changes.

To deploy the my-agent, run the following command:

    gcloud deployment-manager deployments create my-agent --config
    daemonset.yaml


Note that your new deployment is named my-agent.

The biggest advantage of using Deployment Manager templates is that they can be
used together to deploy complex resources under a single deployment.
Maintaining a deployment simply requires updating the yaml configuration and
running an update to your deployment with the new configuration.
