create table newone (select who,what,COUNT(what) cn,number from sssa group by who,what)
