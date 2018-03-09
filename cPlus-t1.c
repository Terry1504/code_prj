/*
#################################################################################
#
# <sequential container>
#
# vector, list, deque
# stack, queue, priority_queue
# container, iterator, adaptor
#
################################################################################

################################################################################
#
# associative container
#
# map, set
#
################################################################################

################################################################################
#
# generic algorithm, sort/unique/etc
# 100+ algorithm: iterator - input/output/forward/bidirectional/random
#
################################################################################

# sort
# - insert sort
# - merge sort
# - quick sort
# - bubble sort

*/

#include <stdlib.h>
#include <stdio.h>

#define NUM 10000
#define MAXDATA 1000

int mergeASort(int y[])
{
    printf("=== start mergeSort === \n");
    int i = 0;
    int startPos = 0;
    int z[NUM];
    int batchSize = 2;
    while (batchSize/2 < NUM)
    {
        /* printf("\n batchSize: %d \n", batchSize); */
        i = 0;
        startPos = 0;
        while (startPos < NUM)
        {
            /* printf("merge %d --> %d --> %d, ", startPos, startPos + batchSize/2, startPos + batchSize - 1); */
            int p1 = startPos;
            int p2 = startPos + batchSize/2;
            while ((p1 < startPos + batchSize/2) && (p2 < startPos + batchSize) && (p2 < NUM))
            {
                if (y[p1] < y[p2])
                {
                    z[i] = y[p1]; i++; p1++;
                }
                else
                {
                    z[i] = y[p2]; i++; p2++;
                }
            }
            if (p1 < startPos + batchSize/2)
            {
                while (p1 < startPos + batchSize/2)
                {
                    z[i] = y[p1]; i++; p1++;
                }
            }
            else
            {
                while ((p2 < startPos + batchSize) && (p2 < NUM))
                {
                    z[i] = y[p2]; i++; p2++;
                }
            }

            startPos = startPos + batchSize;
        }

        /* printf("\n result after batchSize: %d \n", batchSize); */
        for (i = 0; i < NUM; i++)
        {
            y[i] = z[i];
            /* printf("%d -- ", y[i]); */
        }

        batchSize = 2 * batchSize;
    }

    printf("=== end mergeSort === \n");
    for (i = 0; i < NUM; i++)
    {
        printf("%d -- ", y[i]);
    }
    printf("\n");

    return 1;
}


int bubbleSort(int y[])
{
    printf("=== start bubbleSort === \n");

    for (int j = NUM - 1; j >= 0; j--)
        for (int k = 0; k < j; k++)
        {
            if (y[k] > y[k+1])
            {
                int temp;
                temp = y[k+1];
                y[k+1] = y[k];
                y[k] = temp;
            }
        }

    printf("=== end bubbleSort === \n");
    return 1;
}

int selectSort(int y[])
{
    printf("=== start selectSort === \n");

    for (int j = NUM - 1; j >= 0; j--)
    {
        int temp;
        int max = y[j];
        int maxIndex = j;
        for (int k = 0; k < j; k++)
        {
            if (y[k] > max)
            {
                max = y[k];
                maxIndex = k;
            }
        }
        temp = y[j];
        y[j] = max;
        y[maxIndex] = temp;
    }

    printf("=== end selectSort === \n");
    return 1;
}

int insertSort(int y[])
{
    printf("=== start insertSort === \n");

    int z[NUM];
    int i, j, k;
    for (i = 0; i < NUM; i++)
    {
        for (j = 0; j <= i - 1; j++)
        {
            if (z[j] > y[i]) break;
        }
        for (k = i - 1; k >= j ; k--)
        {
            z[k+1] = z[k];
        }
        z[j] = y[i];
    }
    for (i = 0; i < NUM; i++)
    {
        y[i] = z[i];
    }

    printf("=== end insertSort === \n");
    return 1;
}

int quickSort(int y[], int start, int end)
{
    printf("=== start quickSort === \n");

    int temp;

    if (start >= end)
    {
        return -1;
    }

    int p1 = start + 1;
    int p2 = end;

    if (p1 == p2)
    {
        if (y[start] > y[end])
        {
            temp = y[start];
            y[start] = y[end];
            y[end] = temp;
        }
        return 1;
    }

    while (p1 < p2)
    {
        while ((y[p1] <= y[start]) && (p1 <= end) && (p1 <= p2)) { p1++; }
        if (p1 > end)
        {
            temp = y[end];
            y[end] = y[start];
            y[start] = temp;

            quickSort(y, start, end-1);
        }
        else if (p1 > p2)
        {
            temp = y[p2-1];
            y[p2-1] = y[start];
            y[start] = temp;

            quickSort(y, start, p2-2);
            quickSort(y, p2, end);
        }
        else
        {
            while ((y[p2] >= y[start]) && (p2 > start) && (p1 <= p2)) { p2--; }
            if (p2 <= start)
            {
                quickSort(y, start+1, end);
            }
            else
            {
                if (p1 < p2)
                {
                    temp = y[p1];
                    y[p1] = y[p2];
                    y[p2] = temp;
                }
                else if (p1 > p2)
                {
                    temp = y[p1-1];
                    y[p1-1] = y[start];
                    y[start] = temp;

                    quickSort(y, start, p1-2);
                    quickSort(y, p1, end);
                }
            }
        }
    }

    printf("=== end quickSort === \n");
    return 1;
}


int main(int argc, char *argv[])
{

    int x[NUM];

    /* generate initial data */
    for (int i = 0; i < NUM; i++)
    {
        x[i] = random() % MAXDATA;
    }

    printf("========= before sort ========= \n");
    for (int i = 0; i < NUM; i++)
    {
        printf("%d -- ", x[i]);
    }
    printf("\n");

    /* sort */
    /* bubbleSort(x); */
    /* selectSort(x); */
    /* insertSort(x); */
    /* mergeASort(x); */
    quickSort(x, 0, NUM-1); 


    /* print out again */
    printf("========= after sort ========= \n");
    for (int i = 0; i < NUM; i++)
    {
        printf("%d:%d -- ", i, x[i]);
    }
    printf("\n");
    for (int i = 0; i < NUM-1; i++)
    {
        if (x[i] > x[i+1])
        {
            printf("FAIL. %d:%d, %d:%d \n", i, x[i], i+1, x[i+1]);
        }
    }
    printf("PASS. \n");
    printf("\n");

    return 1;

}
