#include <stdio.h>
int main() {
    int dd,mm,yyyy,nday,ny,ly,i,m[12];
    printf("Enter dd mm yyyy:");
    scanf("%d %d %d",&dd,&mm,&yyyy);

    if (yyyy>2022) {
        ny=yyyy-2022;
        ly=ny/4;
        if ((yyyy%4==1) || (yyyy%4==2)) {
            m[0]=31;
            m[1]=28;
            m[2]=31;
            m[3]=30;
            m[4]=31;
            m[5]=30;
            m[6]=31;
            m[7]=31;
            m[8]=30;
            m[9]=31;
            m[10]=30;
            m[11]=31;
            nday=0;
            for (i=0;i<mm-1;i++) {
                nday+=m[i];

            }
            nday+=dd+335+(ny-1-ly)*365+ly*366;
            if (nday%7==0) printf("Sunday\n");
            else if (nday%7==1) printf("Monday\n");
            else if (nday%7==2) printf("Tuesday\n");
            else if (nday%7==3) printf("Wednesday\n");
            else if (nday%7==4) printf("Thursday\n");
            else if (nday%7==5) printf("Friday\n");
            else printf("Saturday\n");
            
        }
        if (yyyy%4==3) {
            ly+=1;
            m[0]=31;
            m[1]=28;
            m[2]=31;
            m[3]=30;
            m[4]=31;
            m[5]=30;
            m[6]=31;
            m[7]=31;
            m[8]=30;
            m[9]=31;
            m[10]=30;
            m[11]=31;
            nday=0;
            for (i=0;i<mm-1;i++) {
                nday+=m[i];

            }
            nday+=dd+335+(ny-1-ly)*365+ly*366;
            if (nday%7==0) printf("Sunday\n");
            else if (nday%7==1) printf("Monday\n");
            else if (nday%7==2) printf("Tuesday\n");
            else if (nday%7==3) printf("Wednesday\n");
            else if (nday%7==4) printf("Thursday\n");
            else if (nday%7==5) printf("Friday\n");
            else printf("Saturday\n");
        }
        if (yyyy%4==0) {
            m[0]=31;
            m[1]=29;
            m[2]=31;
            m[3]=30;
            m[4]=31;
            m[5]=30;
            m[6]=31;
            m[7]=31;
            m[8]=30;
            m[9]=31;
            m[10]=30;
            m[11]=31;
            nday=0;
            for (i=0;i<mm-1;i++) {
                nday+=m[i];

            }
            nday+=dd+335+(ny-1-ly)*365+ly*366;
            if (nday%7==0) printf("Sunday\n");
            else if (nday%7==1) printf("Monday\n");
            else if (nday%7==2) printf("Tuesday\n");
            else if (nday%7==3) printf("Wednesday\n");
            else if (nday%7==4) printf("Thursday\n");
            else if (nday%7==5) printf("Friday\n");
            else printf("Saturday\n");
            
        }
        
    }
    if (yyyy<2022) {
       ny=2022-yyyy;
       ly=ny/4;
       if ((yyyy%4==1) || (yyyy%4==2)) {
           m[0]=31;
            m[1]=28;
            m[2]=31;
            m[3]=30;
            m[4]=31;
            m[5]=30;
            m[6]=31;
            m[7]=31;
            m[8]=30;
            m[9]=31;
            m[10]=30;
            m[11]=31;
            nday=0;
            for (i=mm;i<12;i++) {
                nday+=m[i];
            }
            nday+=m[mm-1]-dd+(ny-ly-1)*365+(ly)*366+30;
            if (nday%7==0) printf("Sunday\n");
            else if (nday%7==1) printf("Saturday\n");
            else if (nday%7==2) printf("Friday\n");
            else if (nday%7==3) printf("Thursday\n");
            else if (nday%7==4) printf("Wednesday\n");
            else if (nday%7==5) printf("Tuesday\n");
            else printf("Monday\n");
       }
       if (yyyy%4==3) {
           ly+=1;
           m[0]=31;
            m[1]=28;
            m[2]=31;
            m[3]=30;
            m[4]=31;
            m[5]=30;
            m[6]=31;
            m[7]=31;
            m[8]=30;
            m[9]=31;
            m[10]=30;
            m[11]=31;
            nday=0;
            for (i=mm;i<12;i++) {
                nday+=m[i];
            }
            nday+=m[mm-1]-dd+(ny-ly-1)*365+(ly)*366+30;
            if (nday%7==0) printf("Sunday\n");
            else if (nday%7==1) printf("Saturday\n");
            else if (nday%7==2) printf("Friday\n");
            else if (nday%7==3) printf("Thursday\n");
            else if (nday%7==4) printf("Wednesday\n");
            else if (nday%7==5) printf("Tuesday\n");
            else printf("Monday\n");
       }
       if (yyyy%4==0) {
            m[0]=31;
            m[1]=29;
            m[2]=31;
            m[3]=30;
            m[4]=31;
            m[5]=30;
            m[6]=31;
            m[7]=31;
            m[8]=30;
            m[9]=31;
            m[10]=30;
            m[11]=31;
            nday=0;
            for (i=mm;i<12;i++) {
                nday+=m[i];
            }
            nday+=m[mm-1]-dd+(ny-ly-1)*365+(ly)*366+30;
            if (nday%7==0) printf("Sunday\n");
            else if (nday%7==1) printf("Saturday\n");
            else if (nday%7==2) printf("Friday\n");
            else if (nday%7==3) printf("Thursday\n");
            else if (nday%7==4) printf("Wednesday\n");
            else if (nday%7==5) printf("Tuesday\n");
            else printf("Monday\n");
       } 
    }
    if (yyyy==2022) {
        
        if ((mm>=2) || ((mm=1) && (dd>=30))) {
            m[0]=31;
            m[1]=28;
            m[2]=31;
            m[3]=30;
            m[4]=31;
            m[5]=30;
            m[6]=31;
            m[7]=31;
            m[8]=30;
            m[9]=31;
            m[10]=30;
            m[11]=31;
            nday=0;
            for (i=0;i<mm-1;i++) {
                nday+=m[i];
            }
            nday=nday+dd-30;
            if (nday%7==0) printf("Sunday\n");
            else if (nday%7==1) printf("Monday\n");
            else if (nday%7==2) printf("Tuesday\n");
            else if (nday%7==3) printf("Wednesday\n");
            else if (nday%7==4) printf("Thursday\n");
            else if (nday%7==5) printf("Friday\n");
            else printf("Saturday\n");
           
        }
        else {
         m[0]=31;
            m[1]=28;
            m[2]=31;
            m[3]=30;
            m[4]=31;
            m[5]=30;
            m[6]=31;
            m[7]=31;
            m[8]=30;
            m[9]=31;
            m[10]=30;
            m[11]=31;
            nday=30-dd;
               if (nday%7==0) printf("Sunday\n");
            else if (nday%7==1) printf("Saturday\n");
            else if (nday%7==2) printf("Friday\n");
            else if (nday%7==3) printf("Thursday\n");
            else if (nday%7==4) printf("Wednesday\n");
            else if (nday%7==5) printf("Tuesday\n");
            else printf("Monday\n");
        }
        
    }
    return 0;

}
