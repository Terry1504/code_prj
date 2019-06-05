#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

pthread_mutex_t m;
int     i;

void func1()
{
        int k;
        for (k = 0; k < 100; k++)
        {
                pthread_mutex_lock(&m);
                printf("func1: %d \n", i);
                i++;
                pthread_mutex_unlock(&m);
                sleep(1);
        }
}

void func2()
{
        int k;
        for (k = 0; k < 100; k++)
        {
                pthread_mutex_lock(&m);
                printf("func2: %d \n", i);
                i++;
                pthread_mutex_unlock(&m);
                sleep(1);
        }
}

int main()
{
        pthread_t thread_id1;
        pthread_t thread_id2;
        pthread_attr_t attr;

        pthread_mutex_init(&m, NULL);
        i = 1;

        pthread_attr_init(&attr);
        pthread_create(&thread_id1, &attr, func1, NULL);
        pthread_attr_init(&attr);
        pthread_create(&thread_id2, &attr, func2, NULL);
        pthread_join(thread_id1, NULL);
        pthread_join(thread_id2, NULL);

        pthread_mutex_destroy(&m);

        return 1;
}
