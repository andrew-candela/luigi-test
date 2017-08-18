# luigi-test
Basic Luigi functions.  
test_easy.py takes a file on disk and copies it somewhere else. Then another step takes that file and copies it again. 
run luigi with  
`>$ luigi --module test_easy  --local-scheduler`

There are a couple of works in progress. If I had to take this and apply it to my workload from MM, I'd make a bunch of tasks that submit spark jobs and write out \_success files on success. That \_success file would be the output of the task and it's dependancies would just check that that exists.
