sequenceDiagram
actor User

box Amazon Services
participant fs as Amazon S3 Bucket
participant SQS
participant db as Dynamo db
end

box Kubernetes Cluster
participant fw as Recipe Watcher Container
participant client as Recipe Sender Container
participant rs as Recipe Server Container
end



activate SQS
activate db
activate fs

User ->> fs: Upload Recipe

    loop Poll every 5 seconds

        activate fw
        fw ->> fs: Get current file list
        fw ->> fw : compare against previous cached files

        opt File list has changed
            fw ->> fw : update file list
            fw ->> SQS: submit upload job
            SQS ->>+ client: Notify of new recipe
            client ->>+ rs: [POST] / recipe/{id}/make
            rs ->> rs: Compare for changes with exisiting recipe
            rs ->>+ db: Create new make object
            db ->>- rs: Created object
            rs ->>- client: [200] OK 
        end 
        deactivate fw
    end

deactivate SQS
deactivate db
deactivate fs
