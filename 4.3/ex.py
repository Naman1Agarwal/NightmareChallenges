undefined8 main(void)

{
  FILE *__stream;
  char *pcVar1;
  long in_FS_OFFSET;
  double dVar2;
  char local_52 [10];
  char local_48 [56];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  fgets(local_52,10,stdin);
  dVar2 = atof(local_52);
  if ((float)dVar2 < 37.359287) {
    puts("Too low just like you\'re chances of reaching the bottom.");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  if (37.359287 < (float)dVar2) {
    puts("Too high just like your hopes of reaching the bottom.");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  __stream = fopen("flag.txt","r");
  while( true ) {
    pcVar1 = fgets(local_48,0x32,__stream);
    if (pcVar1 == (char *)0x0) break;
    printf("%s",local_48);
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
