sequenceDiagram
actor User

box Amazon Services
participant fs as Amazon S3 Bucket
participant SQS

participant fw as Recipe Watcher Lambda
participant client as Recipe Sender Lambda
participant rs as Recipe Server Lambda
participant db as Dynamo db
end





User ->> fs: Upload Recipe



    activate fw
    fs -) fw: Trigger lambda


        fw ->> SQS: submit upload job
        deactivate fw

        activate client
        SQS -)+ client: Trigger lambda
        client ->>+ rs: [POST] / recipe/{id}/make
        rs ->> rs: Compare for changes with exisiting recipe
        rs ->>+ db: Create new make object
        db ->>- rs: Created object
        rs ->>- client: [200] OK 
        deactivate client
    
    

