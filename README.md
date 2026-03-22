# 📂 S3 File Upload Notification System

## 📌 Project Overview
The S3 File Upload Notification System is an event driven AWS solution that automatically sends email notifications whenever a file is uploaded to an Amazon S3 bucket. This project demonstrates serverless architecture using AWS managed services with minimal operational overhead.


## 🛠️ AWS Services Used
- Amazon S3  
- AWS Lambda  
- Amazon SNS  
- Amazon CloudWatch  
- AWS IAM  

---
## 🏗️ Architecture Flow Summary
- User uploads a file to Amazon S3  
- S3 detects object creation event  
- S3 triggers AWS Lambda  
- Lambda extracts file metadata  
- SNS sends email notification  
- CloudWatch logs execution

![MasterHead](https://github.com/user-attachments/assets/febec3e8-d943-4921-afbd-d37b0d30b097)


---
## 🚀 Step by Step Implementation

### 🪣 Step 1. Create an S3 Bucket
1. Open AWS Management Console  
2. Go to Amazon S3  
3. Click Create bucket  
4. Enter a unique bucket name  
5. Choose a region  
6. Keep default settings  
7. Create the bucket  

Purpose  
This bucket stores files uploaded by users.

![MasterHead](https://github.com/user-attachments/assets/610f9079-87eb-4e54-8658-43c9eca8aea7)


### 📢 Step 2. Create an SNS Topic
1. Open Amazon SNS  
2. Click Create topic  
3. Type - Standard  
4. Topic name is S3-Notification-System  
5. Create topic  

Purpose  
SNS sends email notifications when a file is uploaded.

![MasterHead](https://github.com/user-attachments/assets/ad10c823-329b-46ce-a495-7be827a22e32)


### 📧 Step 3. Subscribe Email to SNS Topic
1. Open the SNS topic  
2. Click Create subscription  
3. Protocol - Email  
4. Endpoint - Your email address  
5. Create subscription  
6. Confirm the subscription from your email  

Purpose  
Registers email recipients for notifications.

![MasterHead](https://github.com/user-attachments/assets/8e4e20b6-df90-45b5-872f-e13c5281bb0e)


### 🔐 Step 4. Create an IAM Role for Lambda
1. Go to IAM  
2. Create role  
3. Trusted entity. AWS service  
4. Use case. Lambda  
5. Attach policies  
   - AmazonS3ReadOnlyAccess  
   - AmazonSNSFullAccess  
   - CloudWatchLogsFullAccess  
6. Create role  

Purpose  
Allows Lambda to read S3 events, publish SNS messages, and write logs.


### ⚡ Step 5. Create a Lambda Function
1. Open AWS Lambda  
2. Click Create function  
3. Author from scratch  
4. Function name - s3-notification-lambda  
5. Runtime - Python 3.x  
6. Role - Use existing role  
7. Select the IAM role created earlier
 
![MasterHead](https://github.com/user-attachments/assets/92cb77ba-1a60-4b79-90d3-c27e2b1e868a)


### 🧠 Step 6. Add Lambda Function Code

![MasterHead](https://github.com/user-attachments/assets/a15ab16a-9407-4977-9087-c6617d97e045)


### 🔁 Step 7. Configure S3 Event Trigger
1. Open the S3 bucket  
2. Go to the **Properties** tab  
3. Scroll down to **Event notifications**  
4. Click **Create event notification**  
5. Event name. `file-upload-event`  
6. Event type. **All object create events**  
7. Destination. **Lambda function**  
8. Select your Lambda function  
9. Save changes  

Purpose  
This configuration automatically triggers the Lambda function whenever a new file is uploaded to the S3 bucket.


### 🧪 Step 8. Test the System
1. Open the S3 bucket  
2. Upload any file, for example `test.txt`  
3. The upload automatically triggers Lambda  
4. Lambda publishes a message to SNS  
5. An email notification is sent to the subscribed email address  

Expected Result  
You should receive an email containing the bucket name and uploaded file name.


### 📊 Step 9. Verify CloudWatch Logs
1. Open **Amazon CloudWatch**  
2. Go to **Log groups**  
3. Select the log group for your Lambda function  
4. Review logs to confirm successful execution  

Purpose  
CloudWatch logs confirm that Lambda executed successfully and help with debugging if errors occur.


---


## ⚠️ Challenges Faced and Solutions

### 1. S3 Event Not Triggering Lambda  
**Challenge**  
File upload did not trigger the Lambda function.  

**Solution**  
- Verified S3 event notification configuration  
- Selected **All object create events**  
- Ensured correct Lambda function was attached  
- Checked both services were in the same region  


### 2. Email Notifications Not Received  
**Challenge**  
No email was received after file upload.  

**Solution**  
- Confirmed email subscription from inbox  
- Checked SNS topic ARN in Lambda code  
- Tested SNS manually to verify delivery  
- Ensured Lambda had SNS publish permission  


### 3. Lambda Permission Errors  
**Challenge**  
Lambda failed with access denied error.  

**Solution**  
- Attached correct IAM policies  
  - AmazonS3ReadOnlyAccess  
  - AmazonSNSFullAccess  
  - CloudWatchLogsFullAccess  
- Verified role was linked to Lambda  

---


## 🎯 Learning Outcomes
- Learned event driven architecture using AWS services  
- Implemented serverless automation with AWS Lambda  
- Integrated Amazon S3, Lambda, SNS, and CloudWatch using event triggers  
- Gained hands on experience with AWS monitoring and logging

