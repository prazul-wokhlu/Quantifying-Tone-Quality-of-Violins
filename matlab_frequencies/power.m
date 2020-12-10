function final = power2(audio_file)
    [x,fs] = audioread(audio_file);
    m = length(x);       % original sample length
    n = pow2(nextpow2(m));  % transform length
    y = fft(x,n);
    
    f = (0:n-1)*(fs/n)/10;
    power1 = abs(y).^2/n;      

    final = plot(f(1:floor(n/2)),power1(1:floor(n/2)));
    xlabel('Frequency')
    ylabel('Power')