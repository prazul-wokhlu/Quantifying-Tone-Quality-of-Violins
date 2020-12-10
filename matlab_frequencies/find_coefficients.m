function f = get_coeff(audio_file)
    fundamental = 659.3;
    [sound, soundFs] = audioread(audio_file);
    frameLength = soundFs/fundamental;
    soundDuration = length(sound) * soundFs;
    timeSound = linspace(0, soundDuration,length(sound));
    startingSample =round((soundFs-1)*3+1);
    endingSample = startingSample + frameLength - 1;
    timeSample = timeSound(startingSample:endingSample);
    soundSample = sound(startingSample:endingSample);
    
    for n = 1:10
        cosWeight = 2*fundamental*trapz(timeSample,soundSample.*cos(2*pi*n*fundamental*timeSample));        
        sinWeight = 2*fundamental*trapz(timeSample,soundSample.*sin(2*pi*n*fundamental*timeSample));
        spec(n) = sqrt(cosWeight^2 + sinWeight^2);
    end
    
    for n = 1:10 
        freq(n) = fundamental*n; 
    end
    
    f = table(freq,spec);
 
    
    
        
        
    
    
    