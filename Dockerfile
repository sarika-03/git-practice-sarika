FROM busybox

RUN mkdir sarika
RUN sh -c "cd sarika && echo  " hello my self sarika and i m a devops enginerrr  > hacker.txt " "
RUN ls

COPY . /git-practice-sarika
RUN chmod 755 . /git-practice-sarika

WORKDIR /Downloads

CMD ["cat","hacker.txt"]