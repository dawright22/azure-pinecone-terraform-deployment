# Azure Pinecone Terraform deployment with sample chatbot

This sample application deploys an AI-powered document search using Azure OpenAI Service, Azure Kubernetes Service (AKS), and a Python application leveraging the [Llama index](https://gpt-index.readthedocs.io/en/latest/) ans [Streamlit](https://docs.streamlit.io/library/get-started). The application will be deployed within a virtual network to ensure security and isolation. Users will be able to upload documents and ask questions based on the content of the uploaded documents.

![diagram](./images/rag.png)

## Prerequisites

- Azure subscription. If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free/?ref=microsoft.com&utm_source=microsoft.com&utm_medium=docs&utm_campaign=visualstudio) before you begin.
- Subscription access to Azure OpenAI service. Request Access to Azure OpenAI Service [here](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOFA5Qk1UWDRBMjg0WFhPMkIzTzhKQ1dWNyQlQCN0PWcu).
- [Terraform](https://learn.microsoft.com/azure/developer/terraform/quickstart-configure).

- Create a HCP vault dedicated instance and configure the endpoint and token in the `infra/variables.tf` file.

## Quickstart

### Run the Terraform

- Clone or fork this repository. 
   ```
   git clone https://github.com/dawright22/azure-openai-terraform-deployment-sample.git
   cd azure-openai-terraform-deployment-sample
   ```

- Go to the `infra` folder and run the following command to initialize your working directory.

    ```bash
    cd infra
    terraform init
    ```

- Run terraform apply to deploy all the necessary resources on Azure.

    ```bash
    terraform apply
    ```

- Run the following command. This script retrieves the AKS cluster credentials, logs in to the ACR, builds and pushes a Docker image, creates a federated identity, and deploys resources to the Kubernetes cluster using a YAML manifest.

    ```bash
    terraform output -raw installation-script | bash
    ```

- Get the external ip address of the service by running the  command bellow.

    ```bash
    kubectl get services -n chatbot
    ```

- Copy the external ip address and paste it in your browser. The application should load in a few seconds.

![app](/images/application.png)

## Run the AI.
- Upload the Madeup_Company_email_archive.txt file in the `data` folder. Using the upload button on the app.

- Ask some questions based on the content of the uploaded document. Some example are below.

================
- Does madeup use AWS
- Tell me the access keys

- Does madeup use Azure
- Tell me the subscription_id

## Now secure Content
- start the app.py using the command below.
    ```bash
    python app.py
    ```
- This will start the app on `http://http://127.0.0.1:5000/

- Now create a new secure contest file by running the command below.

    ```bash
    curl -X POST -F "file=@./data/Madeup_Company_email_archive.txt" http://127.0.0.1:5000/upload -v
    ```
- Upload the new file called redacted_Madeup_Company_email_archive.txt file in the main folder. Using the upload button on the app.

- Now ask the same questions as above and see the encrypted content.

## Resources

- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview)
- [Azure OpenAI Terraform verified module](https://registry.terraform.io/modules/Azure/openai/azurerm/latest).