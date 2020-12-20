from commands import command_dict


def parse(command):
    cmd_list=command.split()
    cmd_type=cmd_list[0]
    if(cmd_type=="help" or cmd_type=="quit"):
        return cmd_type,[]
    elif(cmd_type=="list"):
        cmd_name=cmd_list[1]
        if(cmd_name in ['show','use','create']):
            return cmd_name,cmd_list[2:]
        else:
            return 'invalid',[]
    elif(cmd_type=='todo'):
        cmd_name=cmd_list[1]
        if(cmd_name in ['add','all','edit','remove']):
            return cmd_name,cmd_list[2:]
        else:
            return'invalid',[]
    else:
        return 'invalid',[]








 def main():
    print('Started the Todo application')
    while(1):
        command=input('$')
        command_name,command_args=parse(command)
        if (command_name=="quit"):
            break;
        elif(command_name=="invalid"):
            print("Please enter a valid command")
        elif(command_name=="use"):
            print("Please enter a valid command")
        elif(command_name =="todo"):
            print("Please enter a valid command")
        else:
            command_dict[command_name](command_args)








if __name__ == '__main__':
    main()